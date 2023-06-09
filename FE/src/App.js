import './App.css';
import {useState} from 'react';

import React from 'react';
import { createGlobalStyle } from 'styled-components';

import "bootstrap/dist/css/bootstrap.min.css";

import ItemSearch from './ItemSearch';

const GlobalStyle = createGlobalStyle`
  body {
    background: #e9ecef;
  }
`;

function Header(){
  return <header>
    <h1 ><a href="/">LOL_MDC</a></h1>
  </header>
}

function Article1(){
  return <article>
    <h2>Welcome to LOL_MDC</h2>
      LOL_MDC has 4 Component, Expected Team Winning Rate, Expected Of Line Match, Comparison Within Tier and Analysis Skill Damage.
  </article>
}

function Article2(){
  return <article>
    This Page is made by BAD-MDC, People who leave the Air Force training camp for health problems and find a New Way.
  </article>
}

function Nav(props){
  return <nav>
    <ol>
  
    </ol>
  </nav>
}

function Create1(){
  return <article>
    <h2>Expected Team Winning Rate</h2>
    <form>
      <p><input type="text" name="title" placeholder="Champion1"></input></p>
      <p><input type="text" name="title" placeholder="Champion2"></input></p>
      <p><input type="text" name="title" placeholder="Champion3"></input></p>
      <p><input type="text" name="title" placeholder="Champion4"></input></p>
      <p><input type="text" name="title" placeholder="Champion5"></input></p>
      <p><input type = "submit" value = "Caculate"></input></p>
    </form>
  </article>
}

function Create2(){
  return <article>
    <h2>Expected Of Line Match</h2>
    <form>
      <p><input type="text" name="title" placeholder="Champion1"></input></p>
      <p><input type="text" name="title" placeholder="Champion2"></input></p>
      <p><input type = "submit" value = "Caculate"></input></p>
    </form>
  </article>
}

function Create3(){
  return <article>
    <h2>Comparsion Within Tier</h2>
    <form>
      <p><input type="text" name="title" placeholder="Champion1"></input></p>
      <p><input type="text" name="title" placeholder="Champion2"></input></p>
      <p><input type = "submit" value = "Caculate"></input></p>
    </form>
  </article>
}

function Create4(){
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };
  const handleReset = () => {
    setInputValue('');
  };
  const handleSum = () => {
    alert('미구현')
    //inputValue 받아서 계산하는 Code 작성예정
  }

  const handleClick1 = () => {
    setInputValue(inputValue + 'Q');
  };
  const handleClick2 = () => {
    setInputValue(inputValue + 'W');
  };
  const handleClick3 = () => {
    setInputValue(inputValue + 'E');
  };
  const handleClick4 = () => {
    setInputValue(inputValue + 'R');
  };
  const handleClick5 = () => {
    setInputValue(inputValue + '평');
  };

  return <article>
    <h1>Skill</h1>
    <div>
      <p>Select Your Champion and its State</p>
      <img src={`./FE/public/img/Akali.png`} alt=""/>
      <p><input type = 'text' value = {inputValue} onChange={handleInputChange} /></p>
      <button onClick={handleClick1}>Q</button>
      <button onClick={handleClick2}>W</button>
      <button onClick={handleClick3}>E</button>
      <button onClick={handleClick4}>R</button>
      <button onClick={handleClick5}>평타</button>
      <h2>Item Search</h2>
      <ItemSearch />
      <p>Verse.</p>
      <p>Select Your Opposite Champion and its State</p>
      <img src={process.env.PUBLIC_URL + '/img/Aatrox.png'} alt=""/>
      <p><button onClick={handleReset}>Reset</button></p>
      <p><button onClick={handleSum}>Analysis</button></p>
    </div>
  </article>
}

function App() {
  const [mode, setMode] = useState('e');

  let content = null;

  if(mode === 'CREATE1'){
    content = <Create1></Create1>
  }
  else if(mode === 'CREATE2'){
    content = <Create2></Create2>
  }
  else if(mode === 'CREATE3'){
    content = <Create3></Create3>
  }
  else if (mode === 'CREATE4'){
    content = <Create4></Create4>
  }

  return (
    <div>
      <GlobalStyle/>
      <Header></Header>
      <Article1></Article1>
      <Article2></Article2>
      <Nav></Nav>
      
      {content}
      <p><a href="/1. Expected Team Winning Rate" onClick={event=>{
        event.preventDefault();
        setMode('CREATE1');
      }}>Expected Team Winning Rate</a></p>
      <p><a href="/2. Expected Of Line Match" onClick={event=>{
        event.preventDefault();
        setMode('CREATE2');
      }}>Expected Of Line Match</a></p>
      <p><a href="/3. Comparison Within Tier" onClick={event=>{
        event.preventDefault();
        setMode('CREATE3');
      }}>Comparison Within Tier</a></p>
      <p><a href="/4. Skill" onClick={event=>{
        event.preventDefault();
        setMode('CREATE4');
      }}>Skill</a></p>
      
    </div>
  );
}

export default App;
