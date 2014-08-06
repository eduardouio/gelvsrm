<h1>gelvsrm</h1><html>
<p>
	Directorio con la documentacion del sitio, este directorios contiene el modelo de la base de datos,
	se presenta un listado de los ficheros en el sitio
	<ul>
		<li>Readme</li>
		<li>Modelo Gelvsrm</li>
		<li>Diagramas de clases</li>
	</ul>
<p>
La apliación cambia de otientacion, ahira será web y se usará con django, vemoas si es posible usar angularjs en la interfaz de usuario
a trabajar!!!!-.-.
</p>

</p>
Árbol de directorios
<p>
├── aplicacion
│   ├── gelvs
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── polaris
│   │   │   ├── admin.py~
│   │   │   ├── admin.pyc
│   │   │   ├── __init__.py
│   │   │   ├── __init__.pyc
│   │   │   ├── models.py
│   │   │   ├── models.pyc
│   │   │   ├── olds
│   │   │   │   ├── clases
│   │   │   │   │   ├── buyClass.py
│   │   │   │   │   ├── buyTravelClass.py
│   │   │   │   │   ├── cityClass.py
│   │   │   │   │   ├── contactClass.py
│   │   │   │   │   ├── coustumerClass.py
│   │   │   │   │   ├── coustumerClass.pyc
│   │   │   │   │   ├── helper.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── __init__.pyc
│   │   │   │   │   ├── inspectionClass.py
│   │   │   │   │   ├── inventaryClass.py
│   │   │   │   │   ├── invoiceClass.py
│   │   │   │   │   ├── invoiceItemClass.py
│   │   │   │   │   ├── maintenanceClass.py
│   │   │   │   │   ├── maintenanceItemClass.py
│   │   │   │   │   ├── providerClass.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── cityClass.cpython-33.pyc
│   │   │   │   │   │   ├── contactClass.cpython-33.pyc
│   │   │   │   │   │   ├── coustumerClass.cpython-33.pyc
│   │   │   │   │   │   ├── helper.cpython-33.pyc
│   │   │   │   │   │   ├── __init__.cpython-33.pyc
│   │   │   │   │   │   ├── invoiceClass.cpython-33.pyc
│   │   │   │   │   │   ├── maintenanceClass.cpython-33.pyc
│   │   │   │   │   │   ├── repairClass.cpython-33.pyc
│   │   │   │   │   │   ├── stateClass.cpython-33.pyc
│   │   │   │   │   │   └── vehicleClass.cpython-33.pyc
│   │   │   │   │   ├── repairClass.py
│   │   │   │   │   ├── repairItemClass.py
│   │   │   │   │   ├── stateClass.py
│   │   │   │   │   ├── techClass.py
│   │   │   │   │   ├── techTravelClass
│   │   │   │   │   ├── travelClass.py
│   │   │   │   │   └── vehicleClass.py
│   │   │   │   ├── modelo
│   │   │   │   │   ├── conn.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── __init__.pyc
│   │   │   │   │   ├── Modelo.py
│   │   │   │   │   ├── Modelo.pyc
│   │   │   │   │   └── __pycache__
│   │   │   │   │       ├── conn.cpython-33.pyc
│   │   │   │   │       ├── __init__.cpython-33.pyc
│   │   │   │   │       └── Modelo.cpython-33.pyc
│   │   │   │   ├── static_media
│   │   │   │   │   └── files
│   │   │   │   │       ├── css
│   │   │   │   │       │   ├── bootstrap.css.map
│   │   │   │   │       │   ├── bootstrap.min.css
│   │   │   │   │       │   ├── bootstrap-theme.css.map
│   │   │   │   │       │   ├── bootstrap-theme.min.css
│   │   │   │   │       │   └── dashboard.css
│   │   │   │   │       ├── fonts
│   │   │   │   │       │   ├── glyphicons-halflings-regular.eot
│   │   │   │   │       │   ├── glyphicons-halflings-regular.svg
│   │   │   │   │       │   ├── glyphicons-halflings-regular.ttf
│   │   │   │   │       │   └── glyphicons-halflings-regular.woff
│   │   │   │   │       ├── ico
│   │   │   │   │       │   ├── apple-touch-icon-144-precomposed.png
│   │   │   │   │       │   └── favicon.ico
│   │   │   │   │       ├── img
│   │   │   │   │       │   ├── cliente.png
│   │   │   │   │       │   ├── mantenimiento.png
│   │   │   │   │       │   ├── Ranger.png
│   │   │   │   │       │   ├── reparacion.png
│   │   │   │   │       │   └── viaje.png
│   │   │   │   │       └── js
│   │   │   │   │           ├── application.js
│   │   │   │   │           ├── bootstrap.min.js
│   │   │   │   │           ├── customize.min.js
│   │   │   │   │           ├── customizer.js
│   │   │   │   │           ├── docs.min.js
│   │   │   │   │           ├── ie8-responsive-file-warning.js
│   │   │   │   │           ├── raw-files.min.js
│   │   │   │   │           └── vendor
│   │   │   │   │               ├── blob.js
│   │   │   │   │               ├── filesaver.js
│   │   │   │   │               ├── holder.js
│   │   │   │   │               ├── jszip.min.js
│   │   │   │   │               ├── less.min.js
│   │   │   │   │               └── uglify.min.js
│   │   │   │   └── templates
│   │   │   │       ├── head.html
│   │   │   │       └── index.html
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-33.pyc
│   │   │   ├── settings.cpython-33.pyc
│   │   │   ├── urls.cpython-33.pyc
│   │   │   └── wsgi.cpython-33.pyc
│   │   ├── settings.py
│   │   ├── settings.py~
│   │   ├── settings.pyc
│   │   ├── urls.py
│   │   ├── urls.pyc
│   │   ├── wsgi.py
│   │   └── wsgi.pyc
│   ├── __init__.py
│   └── manage.py
├── Documentacion
│   ├── DiagramaControlador.png
│   ├── DiagramaModelo.png
│   ├── Diagramas.zargo
│   ├── Diagramas.zargo~
│   ├── gelvsr.mwb
│   ├── Modelo_a.JPG
│   └── modelo_B.JPG
├── Modelo
│   ├── data_gelvs_rm.sql
│   ├── gelvsrm_polaris.sql
│   ├── insert_detalle_mantenimiento
│   ├── procedimientos_triggers_gelvsrm.sql
│   ├── script_gelvsrm.sql
│   └── vistas_gelvsrm.sql
└── README.md

</p>


