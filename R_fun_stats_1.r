# More stats fun with R
# estimate the correlation coefficient 

x1 = c(1,2,3,10)
x2 = c(34,34,4,5)

df = data.frame(
    x1,
    x2
)

# correlation coefficient 
# r = cov(x1, x2) / sd_x1 * sd_x2

# mean (both x and y)
# covariance(x1, x2) = sum(x1 - x1_mean)*(x2 - x2_mean))/(n-1)
# variance = sum((x1 - x1_mean)^2)/(n-1)
# standard_dev = sqrt(variance)

# expected outcome 
cor(df$x1,df$x2)

# mean function
mu_bar <- function(x) {
    x_mean <- sum(x)/length(x)
}

# variance function
variance <- function(x) {
    var_s = sum((x - mu_bar(x))^2)/(length(x)-1)
    return(var_s)
}

var(df$x1) == variance(df$x1)

# covariance function
covariance <- function(x,y) {
    cov_xy = sum((x-mu_bar(x))*(y-mu_bar(y)))/(length(x)-1)
    return(cov_xy)
}

cov(df$x1,df$x2) == covariance(df$x1,df$x2)

# correlation 
correlation <- function(x1, x2) {
    r = covariance(x1,x2)/sqrt(variance(x1)*variance(x2))
    return(r)     
}

cor(df$x1, df$x2) == correlation(df$x1, df$x2)

# We want to do it within a data frame 
library(tidyverse)
# We want a column for each so we can do some row and column things 
df %>%
    mutate(x1_mu = sum(x1)/length(x1),
           x2_mu = sum(x1)/length(x1),
           var_x1 = sum((x1 - mu_bar(x1))^2)/(length(x1)-1),
           var_x2 = sum((x2 - mu_bar(x2))^2)/(length(x2)-1),
           cov = sum((x1-mu_bar(x1))*(x2-mu_bar(x2)))/(length(x1)-1),
           r = cov/(sqrt(var_x1)*sqrt(var_x2)))
           
####

x1 <- c(11, 21, 4, 5, 66, 8, 9)
median(x1)



median_c <- function(x) {

    x_order <- x[order(x)]

    if(length(x)%%2 != 0) {
        median = x_order[round(length(x)/2,0)]
    } else {
        lower = x_order[round(length(x)/2,0)]
        upper = x_order[round(length(x)/2,0)+1]
        median = (lower + upper) / 2
    }
    return(median)
    }

median(x1) == median_c(x1)

x2 <- c(11, 21, 5, 66, 8, 9)

median(x2) == median_c(x2)

#####
