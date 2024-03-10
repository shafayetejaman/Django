from django.shortcuts import render

# Create your views here.


def index(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "strMealDescription": "BeaverTails, a Canadian specialty, are whole-wheat pastries stretched to resemble beaver tails. They're typically topped with sweet condiments and confections, like whipped cream, banana slices, and chocolate.",
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "strMealDescription": "Breakfast potatoes are a hearty morning meal. They're made from diced, fried potatoes and can be served with a variety of other breakfast dishes, like bacon and eggs.",
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "strMealDescription": "Canadian Butter Tarts are sweet and delicious treats that have a flaky crust and a gooey center. They're a true Canadian delicacy!",
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "strMealDescription": "Montreal Smoked Meat is a type of deli meat made by salting and curing a brisket with spices. The brisket is allowed to absorb the flavors for a week, is hot smoked to cook through, and finally steamed to completion.",
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "strMealDescription": "Nanaimo Bars are a dessert item of Canadian origin popular across North America. It's a bar dessert which requires no baking and is named after the city of Nanaimo, British Columbia.",
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "strMealDescription": "Pate Chinois is a French Canadian dish similar to English cottage pie or shepherd's pie. It's traditionally made with layered ground beef, canned corn, and mashed potatoes.",
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "strMealDescription": "Pouding chomeur, or 'unemployed man's pudding', is a dessert that originated in Quebec during the Great Depression. It's a cake-batter pudding served with a sweet syrup.",
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "strMealDescription": "Poutine is a dish originating from Quebec, Canada, made with french fries and cheese curds topped with a brown gravy.",
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "strMealDescription": "Rappie Pie is a traditional Acadian dish from southwest Nova Scotia and areas of Prince Edward Island. It's a casserole-like meal made from potatoes, meat, and onions.",
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "strMealDescription": "Split Pea Soup is a hearty and nutritious soup made from split peas. It's often flavored with ham and vegetables, making it a popular comfort food.",
        },
    ]

    return render(request, "app1/index.html", {"meals": meals})
