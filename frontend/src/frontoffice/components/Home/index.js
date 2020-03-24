import React from "react";
import { connect } from "react-redux";

import './style.local.scss';




export default
@connect((state, props) => ({}))
class Home extends React.Component {
  componentWillMount() {
    document.title = 'Home'
  }


  render() {

    return (
      //<!-- Document Wrapper -->
      <div className="container">
        <h4>Hello World</h4>
      </div>
    );
  }
}
