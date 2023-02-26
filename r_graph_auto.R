d = Organized_lectin_sequences_from_Frontiers_Brancaccio_2019_1_
browser()
d = t(d)
d = as.data.frame(apply(d,2,as.numeric))
d = d[,colSums(is.na(d)) < nrow(d)]
colnames(d) <- c('length','lg1','lg2','lg3','lg4','lg5','lg13','lg45')

plot_m <- ggplot(d) + geom_blank() + scale_y_continuous(limits = c(-.05,0.5)) 
plot_m <- plot_m + labs(title ='Score vs Length')
plot_m <- plot_m + geom_point(aes(x=length,y=lg1, color = 'lg1'))
plot_m <- plot_m + geom_point(aes(x=length,y=lg2, color = 'lg2'))
plot_m <- plot_m + geom_point(aes(x=length,y=lg3, color = 'lg3'))
plot_m <- plot_m + geom_point(aes(x=length,y=lg4, color = 'lg4'))
plot_m <- plot_m + geom_point(aes(x=length,y=lg5, color = 'lg5'))
plot_m <- plot_m + geom_point(aes(x=length,y=lg13, color = 'lg13'), shape=6)
plot_m <- plot_m + geom_point(aes(x=length,y=lg45, color = 'lg45'))

plot_m <- plot_m + labs(color ='Legend')
plot_m <- plot_m + xlab('n-mer length') + ylab('score')
plot_m                                                                                     

