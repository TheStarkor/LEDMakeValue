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

  Test = () => {
    console.log('123');
    // var citiesRef = this.db.collection("cities");
    // citiesRef.doc("SF").set({
    //   name: "San Francisco", state: "CA", country: "USA",
    //   capital: false, population: 860000,
    //   regions: ["west_coast", "norcal"] });
    // citiesRef.doc("LA").set({
    //   name: "Los Angeles", state: "CA", country: "USA",
    //   capital: false, population: 3900000,
    //   regions: ["west_coast", "socal"] });
    // citiesRef.doc("DC").set({
    //   name: "Washington, D.C.", state: null, country: "USA",
    //   capital: true, population: 680000,
    //   regions: ["east_coast"] });
    // citiesRef.doc("TOK").set({
    //   name: "Tokyo", state: null, country: "Japan",
    //   capital: true, population: 9000000,
    //   regions: ["kanto", "honshu"] });
    // citiesRef.doc("BJ").set({
    //   name: "Beijing", state: null, country: "China",
    //   capital: true, population: 21500000,
    //   regions: ["jingjinji", "hebei"] });
    this.db.collection('Test').doc("Pi").get().then((snap) => {
      console.log(snap.data().Hello);
    });
    this.db.collection("Test").doc("Pi").set({
      Hello: 210
    })
  }

  render() {
    return (
      <div className="home">
        <div className="card w-90" style={{marginTop: '10px'}}>
          <div className="card-body">
            <h5 className="card-title">Name1</h5>
            <p className="card-text">위치: </p>
            <button type="button" class="btn btn-primary" style={{marginRight: '10px'}}>LED</button>
            <button type="button" class="btn btn-danger">Sound</button>
          </div>
        </div>
        <div className="card w-90" style={{marginTop: '10px'}}>
          <div className="card-body">
            <h5 className="card-title">Name2</h5>
            <p className="card-text">위치: </p>
            <button type="button" class="btn btn-primary" style={{marginRight: '10px'}}>LED</button>
            <button type="button" class="btn btn-danger">Sound</button>
          </div>
        </div>
        <div className="card w-90" style={{marginTop: '10px'}}>
          <div className="card-body">
            <h5 className="card-title">Name3</h5>
            <p className="card-text">위치: </p>
            <button type="button" class="btn btn-primary" style={{marginRight: '10px'}}>LED</button>
            <button type="button" class="btn btn-danger">Sound</button>
          </div>
        </div>
      </div>
    )
  }
}

export default Home