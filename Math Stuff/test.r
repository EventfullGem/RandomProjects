# Load the ggplot2 package
library(ggplot2)

# Create a data frame with x and y values
df <- data.frame(x = c(1, 2, 3, 4, 5), y = c(2, 4, 5, 4, 5))

# Create a scatter plot with x and y values
ggplot(df, aes(x = x, y = y)) + 
  geom_point()