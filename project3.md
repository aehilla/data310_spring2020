## Project 3, due April 18

##### Using two machine learning methods predict population values at 100 x 100 meter resolution throughout your selected country. Validate the two models using different methods presented in this class. Write a report assessing the two approaches and which of the two models was more accurate. Be sure to account for spatial variation throughout your selected location and provide substantive explanations for why those variations occurred

For this project, I chose to focus on the Philippines, specifically the regions of Davao del Norte, Davao del Sur, Davao Oriental, and Compostela Valley. 

#### Linear Regression Model:

Population sums plot:

<img src = "https://user-images.githubusercontent.com/54942759/115155197-cea7e380-a04c-11eb-8b24-c37e7a64b830.png" width = 500>

Diff sums plot:

<img src = "https://user-images.githubusercontent.com/54942759/115155316-60afec00-a04d-11eb-97cf-5b10c4151c9b.png" width = 500>

Mean Error:

<img src = "https://user-images.githubusercontent.com/54942759/115155055-1c701c00-a04c-11eb-99fc-c0d1576f873c.png" width = 500>

Mean Absolute Error:

<img src = "https://user-images.githubusercontent.com/54942759/115155083-3f9acb80-a04c-11eb-8bfd-40336b084a56.png" width = 500>

Root Mean Squared Error (3D):

<img src = "https://user-images.githubusercontent.com/54942759/115155124-796bd200-a04c-11eb-94a5-027219608881.png" width = 500>

Cell stats (diff sums): 6016931

#### Random Forest Model:

Population sums plot:

<img src = "https://user-images.githubusercontent.com/54942759/115155496-31e64580-a04e-11eb-89a3-de98fce34500.png" width=500>

Diff sums plot:

<img src = "https://user-images.githubusercontent.com/54942759/115155510-432f5200-a04e-11eb-9b3b-a6a733cc3608.png" width = 500>

Variable importance plot:

<img src="https://user-images.githubusercontent.com/54942759/115155539-7540b400-a04e-11eb-9b06-1d8270068b9c.png" width = 500>

RF Mean Error:

<img src = "https://user-images.githubusercontent.com/54942759/115155701-0adc4380-a04f-11eb-8f4c-ae66898fcf44.png" width = 500>

RF Mean Absolute Error:

<img src = "https://user-images.githubusercontent.com/54942759/115155716-1c255000-a04f-11eb-9d75-4515fd32569d.png" width = 500>

RF Root Mean Squared Error (3D):

<img src="https://user-images.githubusercontent.com/54942759/115155656-f0a26580-a04e-11eb-984f-360f04dcc80c.png" width=500>










