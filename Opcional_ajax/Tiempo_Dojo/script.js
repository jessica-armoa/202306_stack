function dismiss(id) {
  const element = document.querySelector(id);
  element.remove();
}

function changeTemperatures(element_select){
  const span_temperatures = document.querySelectorAll("span.temperature");
  console.log(span_temperatures);
  if(element_select.value == "f"){
    for(let span of span_temperatures){
      span.innerHTML = ((parseInt(span.textContent) * 1.8) + 32).toFixed(2);
    }
  }else{
    for(let span of span_temperatures){
      span.innerHTML = ((parseInt(span.textContent) - 32) / 1.8).toFixed(0);
    }
  }
}

async function getCoderData(ciudad, codigo_pais) {
    var response = await fetch("http://api.openweathermap.org/data/2.5/weather?q="+ciudad+","+codigo_pais+"us&APPID=4b2fb50444462d72d524db313b8ea35e");
    var coderData = await response.json();
    return coderData;
}

async function change(ciudad, codigo_pais){
  //Buscar los campos a cambiar
  var max = document.querySelector("p.max");
  var min = document.querySelector("p.min");
  var description = document.querySelector(".description");
  //Obtener datos
  var datos = await getCoderData(ciudad, codigo_pais);
  console.log(datos)
  //Modificar html
  max.innerHTML = datos.main.temp_max;
  min.innerHTML = datos.main.temp_min;
  description.innerHTML = datos.weather[0].description;
}