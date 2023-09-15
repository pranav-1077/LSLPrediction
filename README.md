# Utilizing AI for Nationwide Lead Water Service Line Prediction
Lead contamination in drinking water, especially harmful to children, prompted the US EPA to mandate public water systems to identify lead service lines (LSL) by Oct 16, 2024 and replace LSL subsequently. Predictive modeling is approved by USEPA as one LSL identification method. However, existing models lack effectiveness in data-scarce regions. This project proposes a cross-regional predictive model fueled by socio-economic, environmental and parcel data. By capturing complex interactions, it improves LSL prediction in data-scarce regions and can potentially revolutionize nationwide LSL identification. This approach aspires to reduce lead in drinking water at an accelerated pace when resources are limited.

1. Datasets \
  a. Conduct a review of existing ML methods used in similar projects \
  b. Assemble a dataset of water service addresses for at least two public water systems (to qualify as a regional model) \
  c. The dataset should include the following features: \
        (i) Property addresses (or lat and long) (this needs to be the anchor to pull other relevant datasets) \
(ii) Construction year and past ownership changes \
(iii) Home price and other home characteristics (# of bedrooms, # of bathrooms, etc.) \
(iv) Year of lead ban \
(v) Other social economic features (children, income, education, upward mobility etc.) \
(vi) Other environmental features (earthquake zone, flooding zone?) \
d. The target features (labels) \
  (i) Confirmation of having a lead service line on the utility side \
  (ii) Confirmation of not having a lead service line on the utility side \
  (iii) Confirmation of having a lead service line on the customer side \
  (iiii) Confirmation of not having a lead service line on the customer side \
e. Conduct data exploration, interpretation, and preparation for the next step \
f. Explore feature construction that reflects the drivers/mechanisms for house owner to replace lead pipeline

2. Modeling \
  a. Explore, train, and evaluate multiple algorithms to select the best model for the project objectives.\
  b. Explore and select services like wandb or MLflow for proper versioning of datasets and models \
  c. Explore interpretation tool to explain what happens in the model, such as DiCE \
  d. Explore and select a suitable model hosting service and create model endpoints.

3. User Interface \
   Create model endpoints to be called from a lead service line map where users can: \
  a. Enter a property address (by typing into a search field or clicking on a parcel on the map) and get back predicted probabilities of the property having a lead service line on the utility side and on the customer side. Click here for an example: https://d2u44yafpgs75b.cloudfront.net/map. \
  b. Upload a list of property addresses in CSV format and receive a predicted lead service line probabilities in downloadable table format: https://app.akkio.com/deployments/xD47fjwIsPZwKcVJywac
