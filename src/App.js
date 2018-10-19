import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
      <User username='alicecold'/>
        <header className="App-header">
        
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
        </header>
      </div>
    );
  }
}

function User(props) {
  return <div className="NavBar"><p>/{props.username}</p></div>
  
}


export default App;
