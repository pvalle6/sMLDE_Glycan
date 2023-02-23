d = Organized_lectin_sequences_from_Frontiers_Brancaccio_2019_1_
browser()
d = t(d)
d = as.data.frame(apply(d,2,as.numeric))
d = d[,colSums(is.na(d)) < nrow(d)]
colnames(d) <- c('length','lg1','lg2','lg3','lg4','lg5','lg13','lg45')

plot_m <- ggplot(d) + geom_blank() + scale_y_continuous(limits = c(-.05,0.5)) + geom_point(aes(x=length,y=lg1))

                                                                                          