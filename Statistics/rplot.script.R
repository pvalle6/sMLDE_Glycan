d = Organized_lectin_sequences_from_Frontiers_Brancaccio_2019_1_
browser()
d = t(d)
d = as.data.frame(apply(d,2,as.numeric))
d = d[, colSums(is.na(d))< nrow(d)]
colnames(d) <- c('length','lg1','lg2','lg3','lg4','lg5','lg13','lg45')

for (x in colnames(d))
  plot(d$length,d$x)
