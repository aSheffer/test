if num_hidden==50:
	print(50)
print('num_hidden:', m.num_hidden)
print('learning rate:', m.lr)
m.train(trainset, testset, ephocs_num=40)

