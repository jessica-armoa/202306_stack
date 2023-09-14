async function getCoderData() {
    // La palabra clave await le permite a JS saber que necesita esperar (wait) hasta que obtenga una respuesta para continua
    var response = await fetch("https://api.github.com/users/adion81");
    // Luego necesitamos convertir los datos en formato JSON
    var coderData = await response.json();
    return coderData;
}

var datos = document.getElementById('datos');
var nombre = document.getElementById('nombre-followers');
var imagen = document.getElementById('imagen')

async function mostrar(){
  data = await getCoderData();
  console.log(data);
  datos.style.display = 'block';
  nombre.innerHTML = data.name+" has "+data.followers+" followers";
  imagen.innerHTML = '<img src="'+data.avatar_url+'" alt="avatar github">';
}