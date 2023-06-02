import React from "react";
import illu from './../illustration.svg'
import './show.css'
const Show=({fetchedData})=>{
console.log(fetchedData)
    return(
    <div className="container">
         
        
         <div className="illustration"><img src={illu} className="illustration" alt="logo" /></div>
         <h1 style={{top: `415px`,left: `280px`}} >Problem: {fetchedData.data.problem} </h1>
         <h1 style={{top: `415px`,left: `280px`}} >Solution: {fetchedData.data.solution} </h1>
    </div>);

}

export default Show;