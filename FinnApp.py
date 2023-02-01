import pickle
import streamlit as st
import streamlit.components.v1 as com

com.html("""

def main():
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Diabetes Checker</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <link rel="stylesheet" href="style.css">

            <!--Fonts-->
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap" rel="stylesheet">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@700&display=swap" rel="stylesheet">
            <!--Fonts-->
        </head>
        <body>
                <div class="description">
                    <p class="title">Diabetes Checker</p>

                    <div class="parent">
                        <div class="character">
                            <img src="/character_1.png" alt="" id="character1" width="520px"
                            height="500px">
                        </div>

                        <div class="description1">
                            <p>
                                Get to evaluate your health your health based on personal medical history and 
                                factors and seek immediate medical care.
                            </p>

                            <p>Complete the form below to get your results:</p>
                            <a href="">
                                <script src="https://cdn.lordicon.com/ritcuqlt.js"></script>
                                <lord-icon
                                    src="https://cdn.lordicon.com/eoabunbr.json"
                                    trigger="loop"
                                    style="width:70px;height:70px">
                                </lord-icon>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="footer">

                </div>
        </body>
        </html>
        """)


             
if __name__=='__main__': 
    main()


