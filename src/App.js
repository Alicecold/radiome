import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <Router>
      <div className="App">
      
      <Route path="/login/callback" component={Callback} />
      <Route path="/user/:user" component={Show} />
        
      </div>
      </Router>
    );
  }
}
const Show = ({ match }) => (
  <User username={match.params.user}/>
);

function User(props) {
  return <div><div className="NavBar">
  
  <p>/{props.username}</p>
  
  </div>
  <header className="App-header"><Body user={props.username}/></header></div>
  
}


class Callback extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false
    };
  }

  updateInput(key, value) {
    // update react state
    this.setState({ [key]: value });
  
    // update localStorage
    localStorage.setItem(key, value);
  };

  componentDidMount() {
    this.updateInput('hej', 'value')
  }

  render() {
    const { error, isLoaded } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return <div>Done!</div>;
    }
  }
}

class Body extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      now: "",
      username: props.user,
      broadcasting: false
    };
  }

  componentDidMount() {
    console.log(this.state.username);
    fetch('http://localhost:8080/' + this.state.username)
    .then((response) => {
      return response.json();
    })
    .then((json) => {
      console.log(JSON.stringify(json));
      const response = json.response;
      if(json.response){
        this.setState({
          isLoaded: true,
          now: response.now,
          broadcasting: response.broadcasting
        });
      }
    }, 
    (error) => {
      this.setState({
        isLoaded: true,
        error
      });
    }
    );
  }

  render() {
    const { error, isLoaded, now, broadcasting, username } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      if(broadcasting){
        return (
          <div>
          <p>
            Now playing: 
          </p>
          <p>
            {now}
          </p>
          </div>
        );
      }else{
        return (
          <div>
          <p>
            {username} is not currently sharing their music. Come back later! 
          </p>
          </div>
        );
      }
    }
  }
}

export default App;
