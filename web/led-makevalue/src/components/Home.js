import React, { Component } from 'react'
import config from "./config";
import firebase from "firebase";

export class Home extends Component {
  constructor(props) {
    super(props);
    firebase.initializeApp(config)
    this.db = firebase.firestore();
    console.log(1)
  }

  Find = () => {
    this.db.collection('Test').doc("Pi").get().then((snap) => {
      console.log(snap.data().Hello);
    });
    this.db.collection("Test").doc("Pi").set({
      Find: 1
    })
    alert('찾는 중!')
  }

  render() {
    return (
      <div className="home">
        <div className="card w-90" style={{marginTop: '10px'}}>
          <div className="card-body">
            <h5 className="card-title">리모컨</h5>
            <button type="button" onClick = {this.Find} class="btn btn-primary">찾아줘!</button>
          </div>
        </div>
        <div className="card w-90" style={{marginTop: '10px'}}>
          <div className="card-body">
            <h5 className="card-title">지갑</h5>
            <button type="button" class="btn btn-primary">찾아줘!</button>
          </div>
        </div>
        <div className="card w-90" style={{marginTop: '10px'}}>
          <div className="card-body">
            <h5 className="card-title">열쇠</h5>
            <button type="button" class="btn btn-primary">찾아줘!</button>
          </div>
        </div>
      </div>
    )
  }
}

export default Home