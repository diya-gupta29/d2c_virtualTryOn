# d2c_virtualTryOn
Our implementation consists of two phases. The first phase was designed such that it calculates the body measurements that is the measurement of shoulder and sleeves. This was done so that the “fitting of the attire” could be performed perfectly and the suitable size for the customer could be figured out easily.
Our second phase mimics a virtual trial room where the user can try on shirts that are available. As of now, the users can try only shirts but we plan on including more accessories as we level up. The user sees how the dress looks on him/her on the screen. As we level up further, we plan on integrating the two phases into a single project so that the first phase helps us calculate the measurements of the person which will help us in finding the most suitable size for the current customer while  we show him/her how the apparel looks on him/her for the customer’s satisfaction.

Clone the repo and install the following dependencies:
OpenCV
Flask

To run Phase2_Body-Measurement:
python main.py -i1 "path to Image1" -i2 "path to Image2" -i3 "path to Image3" -a "Correction_mode"

To run Phase2_Virtual_try_on:
python try_on.py
