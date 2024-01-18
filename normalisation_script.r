library(affy)
library(GEOquery)
library(tidyverse)

process_directory <- function(directory_path, output_directory) {
  cel_folder_path <- file.path(directory_path, "celfiles")
  if (!file.exists(cel_folder_path) || !file.info(cel_folder_path)$isdir) {
    cat("Error: 'celfiles' folder not found in", directory_path, "\n")
    return()
  }
  
  raw.data <- ReadAffy(celfile.path = cel_folder_path)
  normalized.data <- rma(raw.data)
  
  normalized.expr <- as.data.frame(exprs(normalized.data))
  
  gse <- getGEO("GSE6222", GSEMatrix = TRUE)
  
  feature.data <- gse$GSE6222_series_matrix.txt.gz@featureData@data
  feature.data <- feature.data[,c(1,11)]
  
  normalized.expr <- normalized.expr %>%
    rownames_to_column(var = 'ID') %>%
    inner_join(., feature.data, by = 'ID')
  
  output_file <- file.path(directory_path, "normalized_expr.csv")
  write.csv(normalized.expr, file = output_file, row.names = FALSE)
  cat("Processed:", directory_path, "and saved to", output_file, "\n")
}

# Replace with the path to your parent directory
parent_directory <- "/home/vidhan/Desktop/Dummy/Unzipped"

# Get a list of subdirectories in the parent directory
subdirectories <- list.dirs(parent_directory, full.names = TRUE)

# Process each subdirectory
for (subdirectory in subdirectories) {
  process_directory(subdirectory, subdirectory)
}
