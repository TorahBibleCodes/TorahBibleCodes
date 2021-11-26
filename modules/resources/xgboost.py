# finalize model and make a prediction for monthly births with xgboost
from numpy import asarray
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from xgboost import XGBRegressor

# transform a time series dataset into a supervised learning dataset
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols = list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
	# put it all together
	agg = concat(cols, axis=1)
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg.values


def predict(values):
	# load the dataset
	lendata = len(values)
	# transform the time series data into supervised learning
	train = series_to_supervised(values, n_in=lendata -1, n_out=1)
	# split into input and output columns
	trainX, trainy = train[:, :-1], train[:, -1]
	#print(trainX)
	# fit model
	model = XGBRegressor(objective='reg:squarederror', n_estimators=100)
	model.fit(trainX, trainy)
	# construct an input for a new preduction
	#row = values[-10:].flatten()
	row2 = values[:lendata-1]
	#row2 = values
	#print(row2)
	# make a one-step prediction
	adata = asarray([row2])
	yhat = model.predict(adata)
	yhat ='%.3f' % (yhat)
	yhat = str(yhat)
	print(values)

	pred = yhat.split('.')
	print('Input: %s, Expected=%i, Predicted: %s' % (row2, trainy, pred[0]))

