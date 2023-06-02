import React, { useState, useEffect } from "react";
import './choices.css'
import Select from 'react-select'
import { Link } from "react-router-dom";

import axios from 'axios'

import http from "../http-common";

const Choices = ({ os, setProblemH, setFetchedData,setProblemS, setProblemB, problemH, problemS, problemB }) => {

  const list = document.querySelectorAll('.select');
  list.forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelector('.change')?.classList.remove('change')
      btn.classList.add('change');
    })
  })

  const hard = [
    { value: 'none', label: 'none' },
    { value: 'Hard Drive', label: 'Hard Drive' },
    { value: 'Memory', label: 'Memory' },
    { value: 'Power Supply', label: 'Power Supply' },
    { value: 'Network Adapter', label: 'Network Adapter' },
    { value: 'Graphics Card', label: 'Graphics Card' },
    { value: 'Motherboard', label: 'Motherboard' },
    { value: 'RAM', label: 'RAM' }
  ]
  const soft = [
    { value: 'none', label: 'none' },
    { value: 'Operating System', label: 'Operating System' },
    { value: 'Application software', label: 'Application software' }
  ]
  const boot = [
    { value: 'none', label: 'none' },
    { value: 'Slow', label: 'Slow' },
    { value: 'Blue screen', label: 'Blue screen' },
    { value: 'no power', label: 'no power' },
    { value: 'No Internet Connection', label: 'No Internet Connection' },
    { value: 'No Bootable device', label: 'No Bootable device' },
    { value: 'Display issues', label: 'Display issues' },
    { value: 'System Freezzes', label: 'System Freezzes' },
    { value: 'Frequent Crashes', label: 'Frequent Crashes' },
    { value: 'Disk Read Error', label: 'Disk Read Error' },
    { value: 'Artifacts on screen', label: 'Artifacts on screen' },
    { value: 'Crashes on launch', label: 'Crashes on launch' },
    { value: 'Limeted Connectivity', label: 'Limeted Connectivity' }
  ]
  const [data, setData] = useState("");


  const handleClickProblem = () => { }
  let hardV="hard drive"
  let softV="operating system"
  let bootV="None"
  const res = async () => {
    console.log(problemH, problemS, problemB)
  
    http.get(`?category=${problemH.toLowerCase()}&software_type=${problemS.toLowerCase()}&boot_status=${problemB.toLowerCase()}`).then(data=>{ setFetchedData(data) ; console.log(data)
       })
      }
      
      useEffect(() => {
       console.log("test", setFetchedData);
     }, [setFetchedData])

  // useEffect(() => { res(); }, [setFetchedData])

  return (
    <div className="container">

      <div > <p style={{ top: `20px`, left: `240px`, fontSize: `19px`, color: `#e07a5f` }}>You selected {os} as an operating system!</p></div>
      <p style={{ top: `60px`, left: `160px`, fontSize: `28px` }}> Select the Hardware problem you're facing!</p>

      <select className="se" style={{ top: `180px` }} onChange={(e) => { setProblemH(e.target.value) }}>
        {hard.map(o => (
          <option value={o.value}>{o.label} </option>
        ))}
      </select>

      <p style={{ top: `110px`, left: `160px`, fontSize: `28spx` }}> Select the software problem you're facing!</p>

      <select className="se" style={{ top: `290px` }} onChange={(e) => { setProblemS(e.target.value) }}>
        {soft.map(o => (
          <option value={o.value}>{o.label} </option>
        ))}
      </select>

      <p style={{ top: `160px`, left: `160px`, fontSize: `28px` }}> Select the Boot problem you're facing!</p>

      <select className="se" style={{ top: `420px` }} onChange={(e) => { setProblemB(e.target.value) }}>
        {boot.map(o => (
          <option value={o.value}>{o.label} </option>
        ))}
      </select>




      <Link className="btn" to="/Result" style={{ left: `260px`, top: `530px`, color: `transparent` }} onClick={res}><h3 style={{ left: `65px`, color: `#e07a5f` }}>Show The Problem</h3></Link>

    </div>);

}

export default Choices;