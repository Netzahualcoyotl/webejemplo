def establecer_estilos():
    estilos = """
    body {
      background-image: url("/static/imagenes/fondo/logo_ipn_guinda.svg");
      background-size: cover;
      background-position: center center;
      background-repeat: no-repeat;
    }
    .logo {
      position: absolute;
      top: 0;
      left: 0;
      height: 50px;
      width: 50px;
      background-image: url("imagenes/icono/logo_ipn_guinda.svg");
      background-repeat: no-repeat;
      background-size: contain;
     }

    h1 {
      color: #3f3f3f;
    }

    body {
      font-family: Arial, sans-serif;
    }

    nav {
      background-color: #f2f2f2;
      padding: 20px;
    }

    nav ul {
      list-style: none;
      margin: 0;
      padding: 0;
    }

    nav ul li {
      display: inline-block;
      margin-right: 10px;
    }

    nav ul li a {
      color: #3f3f3f;
      text-decoration: none;
      padding: 10px;
    }

    nav ul li a:hover {
      background-color: #3f3f3f;
      color: #f2f2f2;
    }
    """
    estilos2 = """
    body {
      background-color: #F5F5F5;
      font-family: Arial, sans-serif;
    }
    h1 {
      color: #3f3f3f;
      text-align: center;
    }
    table {
      border-collapse: collapse;
      width: 100%;
    }
    th, td {
      padding: 8px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }
    tr:hover {
      background-color:#f5f5f5;
    }
    """
    estilos3 = """
     .logo {
         position: absolute;
         top: 0;
         left: 0;
         height: 50px;
         width: 50px;
         background-image: url("imagenes/icono/logo_ipn_guinda.svg");
         background-repeat: no-repeat;
         background-size: contain;
      }
    body {
        background-color: #FFFFFF;
        color: #fff;
      }
      h1 {
        font-size: 3em;
        text-align: center;
        padding: 50px 0;
      }
      table {
        border-collapse: collapse;
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        border: 3px solid #fff;
      }
      th, td {
        padding: 10px;
        text-align: center;
        border: 1px solid #fff;
      }
      th {
        background-color: #fff;
        color: #FF00FF;
        font-size: 1.5em;
        text-transform: uppercase;
      }
      tr:nth-child(even) {
        background-color: #e5e5e5;
      }
      button[type="submit"] {
        display: block;
        margin: 0 auto;
        padding: 10px;
        background-color: #fff;
        color: #960018;
        border: none;
        font-size: 1.2em;
        cursor: pointer;
        transition: all 0.2s ease;
      }
      button[type="submit"]:hover {
        background-color: #960018;
        color: #fff;
      }
    """
    estilos4 = """
     /* Estilo para el fondo blanco */
    body {
      background-color: #fff; 
    }
    
    /* Estilo para la tabla guinda */
    table {
      border-collapse: collapse;
      width: 100%;
      max-width: 800px;
      margin: 20px auto;
      background-color: #8C1D40;
      color: #fff;
    }
    
    /* Estilo para las celdas de la tabla */
    td, th {
      padding: 10px;
      text-align: center;
      border: 1px solid #fff;
    }
    
    /* Estilo para los encabezados de la tabla */
    th {
      background-color: #E1A12C;
    }
    
    /* Estilo para los botones */
    button {
      background-color: #E1A12C;
      border: none;
      color: #fff;
      padding: 10px;
      margin-top: 20px;
      cursor: pointer;
    }
    
    button:hover {
      background-color: #8C1D40;
    }
    
    /* Estilo para el encabezado */
    h1 {
      text-align: center;
      color: #8C1D40;
      margin-top: 50px;
    }
    
    /* Estilo para el mensaje de no resultados */
    td[colspan] {
      text-align: center;
    }
    """

    return {'estilos' : estilos, 'estilos2' : estilos2, 'estilos3' : estilos3, 'estilos4' : estilos4}
    
