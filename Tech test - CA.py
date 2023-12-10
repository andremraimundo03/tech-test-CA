*** Settings ***
Library           SeleniumLibrary
Library           Collections

*** Variables ***
${BROWSER}        Chrome
${BASE_URL}       http://automationexercise.com
# Variaveis dos aritgos
${PROD_1}    Men T-Shirt
${PROD_2}    Green Side Placket Detail T-Shirt

*** Test Cases *** ***
    # Navigate to page
Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window

    # Ir para o menú 'Products'
    Click Link    Products

    # Validar barra de pesquisa
    ${search_bar_visible}    Element Should Be Visible    xpath=//input[@id='search']
    Run Keyword If    not ${search_bar_visible}    Fail    Search bar is not visible

    # Procurar por 'men tshirt' 
    Input Text    xpath=//input[@id='search']    ${PROD_1}

    # Search button
    Click Button    xpath=//button[@class='search-button']

    # Validar "men t-shirt"
    ${search_result_visible}    Wait Until Element Is Visible    xpath=//h1[contains(text(),'Search results')]
    Run Keyword If    not ${search_result_visible}    Fail    Search results not visible

    # Add 1 produto
    Add Product To Cart    ${PROD_1}

    # Add 2 produto
    Add Product To Cart    ${PROD_2}

    # Go to 'Cart'
    Click Element    xpath=//a[@class='cart-contents']

    # Validar produtos no carrinho
    ${products_in_cart}    Get WebElements    xpath=//td[@class='product-name']
    Log    Products in Cart: ${products_in_cart}
    Should Contain    ${products_in_cart}    ${PROD_1}
    Should Contain    ${products_in_cart}    ${PROD_2}

    # Validar soma dos produtos
    ${total_price}    Get Text    xpath=//span[@class='woocommerce-Price-amount amount']
    Log    Total Price: ${total_price}
    Should Be Equal As Numbers    ${total_price.replace('€', '')}    1400.00

*** Keywords ***
Add Product To Cart
    [Arguments]    ${locator}
    Click Element    xpath=${locator}
    Click Button    xpath=//button[@name='add-to-cart']
