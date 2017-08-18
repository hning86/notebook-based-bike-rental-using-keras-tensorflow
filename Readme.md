# Bike Rental in Notebook using Keras/Tensor Flow #


This project shows how to setup LSTM based network for estimating bike rental demand and operationalize it.



- Execute every cell in the notebook
- Once all the cells are executed, operationalize using the following commands



### Setup Environment ###


- Setup local environment

```

	az ml env setup 
	az ml env local

```

### Deploy ###


- Publish web service

```

	az ml service create realtime -f bikescore.py -s bikeschema.json --model-file finalmodel.sav --model-name bikemodel -n bikews -r spark-py -c conda_dependencies.yml -l

```

- List web service


```

	az ml service show realtime -n bikews

```

### Consume ###


- Consume web service

```

	 az ml service run realtime -n bikews -d "{\"npa\": [[450.0, 353.0, 285.0, 332.0, 377.0, 268.0, 218.0, 387.0, 834.0, 508.0, 153.0, 42.0, 4.0, 1.0, 10.0, 17.0, 0.0, 4.0, 1.0, 2.0, 0.58, 0.5455, 0.64, 0.3284], [890.0, 450.0, 353.0, 285.0, 332.0, 377.0, 268.0, 218.0, 387.0, 834.0, 508.0, 153.0, 4.0, 1.0, 10.0, 18.0, 0.0, 4.0, 1.0, 2.0, 0.56, 0.5303, 0.64, 0.3284], [788.0, 890.0, 450.0, 353.0, 285.0, 332.0, 377.0, 268.0, 218.0, 387.0, 834.0, 508.0, 4.0, 1.0, 10.0, 19.0, 0.0, 4.0, 1.0, 2.0, 0.56, 0.5303, 0.68, 0.2985]]}"

```