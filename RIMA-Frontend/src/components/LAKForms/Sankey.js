import React, { Component, Fragment,useState } from "react";
import { toast } from "react-toastify";
import Loader from "react-loader-spinner";
import RestAPI from "services/api";
import axios from "axios";
import Select from 'react-select';

import "d3-transition";
import { select } from "d3-selection";
//import Plot from "react-plotly.js"
import { handleServerErrors } from "utils/errorHandler";

import { Dropdown, Label, Modal, ModalBody, ModalFooter } from "reactstrap";
import { TwitterTweetEmbed } from "react-twitter-embed";

import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";
import "tippy.js/dist/tippy.css";
import "tippy.js/animations/scale.css";
import ReactWordcloud from "react-wordcloud";
import InnerHTML from 'dangerously-set-html-content';
/* Chart code */
// Themes begin
// Themes end

import {
    Button,
    Card,
    CardTitle,
    Progress,
    CardSubtitle,
    CardText,
    CardLink,
    CardBody,
    Collapse,
    FormGroup,
    Form,
    Spinner,
    Input,
    InputGroupAddon,
    InputGroupText,
    InputGroup,
    Row,
    UncontrolledDropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
    ListGroup,
    ListGroupItem,
    Col
  } from "reactstrap";

window.$value='' 

  
 
 
class Sankey extends Component {
  constructor(props){
    super(props);
   
    
    this.clickData=this.clickData.bind(this)
  
    this.state={
     
      isLoaded:false,
      
      items_y1: [],
      items_y2: [],
      items_y12: [],
      arr_keys:[],
      arr_vals:[],
      length:0,
      selectValue2:"",
      selectVal:"",
      desc:"",
      div:"",
      data:[],
    
 
  

    }
  }
 

    
  componentDidMount(){
    //console.log("the json is ******************")    
    this.setState({
        isLoaded:true
    }) 
  };


  
  clickData() {
    
    fetch("http://127.0.0.1:8000/api/interests/topicoverview/")
        .then(response =>  response.json())
        .then(json => {
            this.setState({
                
              items_y1:json.overview,
              
              isLoaded:true
              
              
            })            
        });

    
    
    
  };

  
  

  
  
     
 
      render() {
        

        var {isLoaded,items,arr_keys,arr_vals,items_y1,desc,selectValue2,selectVal} = this.state;
        
       
       
       
      
        
        
       
        

        
        
        
        
        //var{items,arr_keys,arr_vals}=this.state;
        


        
        
        
        if(isLoaded){
        
          return (
            <>
           
            
            <div >
                        
                        
                        
                        <h3>Topic Cloud</h3>
                        <br></br>
                       
                        
                        
              </div>
              {console.log(items_y1)}
           
          
          <br></br>
                        
              
              
             
        
             
              <React.Fragment>
              
              <Row>
                        <Button onClick={this.clickData}>Generate</Button>
                        </Row>
                      
              
            

              
              
              
         
                
              </React.Fragment>
            </>
          );
          } 
        else{
          return (
          <>
        <Button onClick={this.clickData}>Generate</Button>
          </>
          )
        } 
       
      }
}

export default Sankey;