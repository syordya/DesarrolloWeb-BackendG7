const BASE_URL="http://localhost:5000/";
export const crearParticipantes=async(data) =>{
    const result=await fetch(BASE_URL+"participantes",{
        method:"POST",
        headers: {"content-type":"application/json"},
        body:JSON.stringify(data)
    });
    const respuesta=await result.json();
    return respuesta;

};