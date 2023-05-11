import './App.css';
import {useState} from 'react';

function Header(){
  return <header>
    <h1 ><a href="/">LOL_MDC</a></h1>
  </header>
}

/*function Article(){
  return <article></article>
}*/

function Article1(){
  return <article>
    <h2>Welcome to LOL_MDC</h2>
      LOL_MDC has 3 Component, Expected Team Winning Rate, Expected Of Line Match, and Comparison Within Tier.
  </article>
}

function Article2(){
  return <article>
    This Page is made by BAD-MDC, People who leave the Air Force training camp for health problems and find a New Way.
  </article>
}

function Article3(){
  return <article>
    임재성 학과장님 나빠요
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

function App() {
  const [mode, setMode] = useState('d');

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

  return (
    <div>
      <Header></Header>
      <Article1></Article1>
      <Article2></Article2>
      <Article3></Article3>
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
      
    </div>
  );
}

export default App;
