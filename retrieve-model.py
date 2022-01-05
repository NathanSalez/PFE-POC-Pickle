import pickle
import numpy as np
import sklearn

entry = {
	"seplen": 3.0,
	"sepwid": 1.0,
	"petlen": 5.0,
	"petwid": 2.0,
}

to_predict = np.array(list(entry.values())).reshape(1,4)

loaded_model = pickle.load(open("model.pkl","rb"))

result = loaded_model.predict(to_predict)

print(result)
