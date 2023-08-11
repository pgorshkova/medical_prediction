from django.conf import settings
from numpy import array


def make_heart_prediction(data: list) -> str:
    """Making predictons using learning model."""
    model = settings.MODEL
    np_data = array(data)
    np_data_reshaped = np_data.reshape((1, -1))
    prediction = model.predict(np_data_reshaped)
    if prediction[0] > 0.5:
        return 'Heart Failure'
    return 'No Heart Failure'
