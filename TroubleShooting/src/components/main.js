import React from'react'
import './main.css'
import { Link } from "react-router-dom";

const First=({setOs})=>{
  const list=document.querySelectorAll('.select');
  list.forEach(btn=>{btn.addEventListener('click',()=>{
    document.querySelector('.change')?.classList.remove('change')
    btn.classList.add('change');
  })})
    return(
      <div className='container'>
        <h1 style={{color:`#e07a5f`}}>TroubleShooting</h1>
        <p>Choose your operating system </p>
        <div  className="select"  onClick={()=>setOs("windows") } > 
              <h2>Windows</h2>
        </div> 

        <div  className="select" style={{top: `320px`}}  onClick={()=>setOs("Linux") }> 
              <h2>Linux</h2>
        </div> 

        <div  className="select" style={{top: `390px`}} onClick={()=>setOs("macOS") }> 
              <h2>macOS</h2>
        </div> 


        <Link className="btn" to="/Problem" style={{left:`250px` , top:`530px` ,color:`transparent`}}><h3 style={{left:`110px`,color:`#e07a5f`}}>NEXT</h3></Link>
      </div>
    );

}

export default First;