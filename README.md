<h1 id="cli-crud-music">🎵 Cli-Crud-Music</h1>

<p><strong>Cli-Crud-Music</strong> es una aplicación de línea de comandos (CLI) desarrollada en Python que permite gestionar una biblioteca musical hecha como ejercicio en clase en el Master de Big Data e IA. Ofrece funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar) para administrar canciones y artistas en una base de datos MySQL.</p>

<h2 id="caracteristicas">🚀 Características</h2>

<ul>
    <li>📌 Añadir nuevas canciones y artistas a la biblioteca.</li>
    <li>📜 Listar todas las canciones y artistas disponibles.</li>
    <li>✏️ Actualizar información existente de canciones y artistas.</li>
    <li>🗑️ Eliminar canciones o artistas de la biblioteca.</li>
    <li>🔍 Buscar canciones por título o artistas por nombre.</li>
</ul>

<h2 id="instalacion">🛠️ Instalación</h2>

<h3 id="clonar">1️⃣ Clonar el repositorio</h3>

<pre><code>git clone https://github.com/cberdejo/Cli-Crud-Music.git
cd Cli-Crud-Music
</code></pre>

<h3 id="configurar-base-de-datos">2️⃣ Configurar la base de datos MySQL</h3>

<p>Utiliza Docker para preparar la base de datos:</p>

<pre><code>docker run --name cli-crud-music-db -e MYSQL_ROOT_PASSWORD=tu_contraseña -d -p 3306:3306 mysql:latest
</code></pre>

<p>Asegúrate de reemplazar <code>tu_contraseña</code> por una contraseña segura para el usuario root de MySQL.</p>

<h3 id="instalar-dependencias">3️⃣ Instalar dependencias</h3>

<p>Se recomienda utilizar un entorno virtual para gestionar las dependencias de Python:</p>

<pre><code>python3 -m venv venv
source venv/bin/activate  # En Windows, usa venv\Scripts\activate
pip install -r requirements.txt
</code></pre>

<h3 id="configurar-variables-entorno">4️⃣ Configurar variables de entorno</h3>

<p>Copia el archivo <code>.env-template</code> a <code>.env</code> y completa las variables necesarias, como las credenciales de la base de datos.</p>

<pre><code>cp .env-template .env
</code></pre>

<p>Luego, edita el archivo <code>.env</code> con tus credenciales y configuraciones específicas.</p>

<h2 id="uso">📋 Uso</h2>

<p>Una vez completada la instalación y configuración, puedes ejecutar la aplicación con:</p>

<pre><code>python main.py
</code></pre>

<p>Sigue las instrucciones en pantalla para interactuar con la biblioteca musical a través de la línea de comandos.</p>



<h2 id="licencia">📜 Licencia</h2>

<p>Este proyecto está bajo la <strong>Licencia MIT</strong>. Consulta el archivo <a href="LICENSE">LICENSE</a> para más detalles.</p>

