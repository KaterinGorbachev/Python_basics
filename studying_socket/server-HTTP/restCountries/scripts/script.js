import * as countryNameCheck from './isValidCountryName.js'

const api = 'https://restcountries.com/v3.1/name'
const pais_input_field = document.getElementById('pais')
const data_div = document.querySelector('.container')
const list_countries = document.getElementById('list-countries')
const fragment = document.createDocumentFragment()

const check_empty_string = (input_field)=>{
    // if validation functions are only ever called on form .value
    //  don’t need to check typeof str !== 'string'
    if (input_field.value.trim() == ''){
        return { valid: false, error: 'Olvidaste ingresar algo 🚨' }
        
    }
    return { valid: true };

}



let getDataPais = async (pais, api)=>{
    try{
        let respuesta = await axios.get(`${api}/${pais}`)
        return respuesta.data[0]

    }
    catch(error){
        Swal.fire({
            title: `${error}`,
            icon: 'error' 
        })
        return null

    }
    
}

let listenerGetCountry = ()=>{
    data_div.innerHTML=''
        
    if(!check_empty_string(pais_input_field).valid){
        Swal.fire({
            title: `${check_empty_string(pais_input_field).error}`,
            icon: 'error' 

        })
        return
    }
        
    let input_pais = pais_input_field.value.trim()
    let valid = countryNameCheck.isValidCountryName(input_pais.toLowerCase(), countryNameCheck.list_countries)
        
    if(!valid.valid){
        Swal.fire({
            title: `${valid.error}`,
            icon: 'error' 

        })
        return
    }

    getDataPais(input_pais, api).then((datosPais)=>{
            
        let language = ''
        Object.keys(datosPais.languages).forEach(k => {
                
            language += ' '+datosPais.languages[k]
                
        });
        let continent = ''
        Object.keys(datosPais.continents).forEach(k => {
                
            continent += ' '+datosPais.continents[k]
                
        });
        let moneda = Object.keys(datosPais.currencies)[0]

        data_div.innerHTML=`
            <div class="img-box">
                <img src="${datosPais.flags.png}" alt="${datosPais.flags.alt}">
            </div>
            <div class="description-pais">
                <p><strong>Nombre:</strong> ${datosPais.name.common}</p>
                <p><strong>Moneda:</strong> ${moneda}</p>
                <p><strong>Idioma:</strong> ${language}</p>
                <p><strong>Continent:</strong> ${continent}</p>
            </div>
        `
        data_div.style.border = 'solid 2px #dadadaff'
        data_div.style.background = '#efefefff'

    }).catch(error=>{
        console.log(error);
            
    })


}


pais_input_field.addEventListener('input', () => {
    const name_letters = pais_input_field.value.toLowerCase();

    // Clear previous results
    list_countries.innerHTML = '';

    if (name_letters === '') return; // don't search if input is empty

    const hint_countries = countryNameCheck.list_countries.filter(country =>
        country.name.toLowerCase().includes(name_letters)
    );
    let anyVisible = false
    if (hint_countries.length > 0) {
        hint_countries.forEach(country => {
            const li = document.createElement('li');
            li.textContent = country.name;
            fragment.appendChild(li);
            li.style.display = ''
            li.addEventListener('mousedown', (e) => {
                e.preventDefault(); 
                pais_input_field.value = li.textContent;
                list_countries.style.display = 'none';
                listenerGetCountry();
            });
        });
        anyVisible = true;
        list_countries.appendChild(fragment)

        
    } 
    list_countries.style.display = anyVisible ? 'flex' : 'none';
});




pais_input_field.addEventListener('keypress', (e)=>{
    if(e.key == 'Enter'){
        list_countries.style.display = 'none';
        data_div.innerHTML=''
        
        if(!check_empty_string(pais_input_field).valid){
            Swal.fire({
                title: `${check_empty_string(pais_input_field).error}`,
                icon: 'error' 

            })
            return
        }
        
        let input_pais = pais_input_field.value.trim()
        let valid = countryNameCheck.isValidCountryName(input_pais.toLowerCase(), countryNameCheck.list_countries)
        
        if(!valid.valid){
            Swal.fire({
                title: `${valid.error}`,
                icon: 'error' 

            })
            return
        }

        getDataPais(input_pais, api).then((datosPais)=>{
            
            let language = ''
            Object.keys(datosPais.languages).forEach(k => {
                
                language += ' '+datosPais.languages[k]
                
            });
            let continent = ''
            Object.keys(datosPais.continents).forEach(k => {
                
                continent += ' '+datosPais.continents[k]
                
            });
            let moneda = Object.keys(datosPais.currencies)[0]

            data_div.innerHTML=`
                <div class="img-box">
                    <img src="${datosPais.flags.png}" alt="${datosPais.flags.alt}">
                </div>
                <div class="description-pais">
                    <p><strong>Nombre:</strong> ${datosPais.name.common}</p>
                    <p><strong>Moneda:</strong> ${moneda}</p>
                    <p><strong>Idioma:</strong> ${language}</p>
                    <p><strong>Continent:</strong> ${continent}</p>
                </div>
            `
            data_div.style.border = 'solid 2px #dadadaff'
            data_div.style.background = '#efefefff'

        }).catch(error=>{
            console.log(error);
            
        })


    }
})



