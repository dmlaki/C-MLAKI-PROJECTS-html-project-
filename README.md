# C-MLAKI-PROJECTS-html-project-images
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Images</title>
    <style>
        /* CSS for styling the page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        nav {
            background-color: #f4f4f4;
            padding: 10px;
            text-align: center;
        }
        nav ul {
            list-style-type: none;
            padding: 0;
        }
        nav ul li {
            display: inline;
            margin-right: 20px;
        }
        section {
            padding: 20px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-gap: 20px;
        }
        .gallery img {
            width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
<header>
    <h1>Please Click here to view more Images</h1>
</header>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#gallery">Gallery</a></li>
            <li><a href="#menu">Menu</a></li>
        </ul>
    </nav>

    <p>Click on the images below:</p>

    <a href="C:\MLAKI\PROJECTS\html project\technology.jpg">
        <img src="C:\MLAKI\PROJECTS\html project\technology.jpg" alt="Image 1">
    </a>
    <p>Above Image tells about technology</p>
    <br>

    <a href="C:\MLAKI\PROJECTS\html project\food.jpg">
        <img src="C:\MLAKI\PROJECTS\html project\food.jpg" alt="Image 2">
    </a>
    <p>Above Image tells about food</p>
    <br>

    <a href="C:\MLAKI\PROJECTS\html project\nature.jpg">
        <img src="C:\MLAKI\PROJECTS\html project\nature.jpg" alt="Image 3">
    </a>
    <p>Above Image tells about nature</p>


    <section id="home">
        <h2>Home</h2>
        <p>Welcome to our website! We provide information about technology and delicious food.</p>
        <a href="#gallery"><img src="technology.jpg" alt="Technology" style="width: 300px; height: auto;"></a>
    </section>

    <section id="gallery">
        <h2>Gallery</h2>
        <div class="gallery">
            <a href="nature.jpg"><img src="nature.jpg" alt="Nature 1"></a>
            <a href="image2.jpg"><img src="image2.jpg" alt="Nature 2"></a>
            <a href="image3.jpg"><img src="image3.jpg" alt="Nature 3"></a>
            <!-- Add more images here -->
        </div>
    </section>

    <section id="menu">
        <h2>Menu</h2>
        <ul>
            <li><a href="burger.jpg">Burger</a></li>
            <li><a href="pizza.jpg">Pizza</a></li>
            <li><a href="salad.jpg">Salad</a></li>
            <!-- Add more food items here -->
        </ul>
    </section>


</body>
</html>
