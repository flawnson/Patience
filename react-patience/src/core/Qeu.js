import React from "react"

import FormInput from "../components/inputs/FormInput.js"
import logo from "../Ouroboros.svg";


export default class Qeu extends React.Component () {
    constructor () {
        super()
        this.state = {
            toggle: false
        }
        this.handleEnter = this.handleEnter.bind(this)
        this.handleToggle = this.handleToggle.bind(this)
    }

    handleEnter () {


    }

    handleToggle () {
        this.setState({toggle: true})
    }

    render () {
        return (
        <div className='component-container' >
            {
                !this.state.toggle
                    ?
                    /*Logic for manual ID input*/
                    <div className='landing-wrapper' >
                        <div className='logo-container' >
                            {/*Logo*/}
                            <img src={logo} className="App-logo" alt="logo"/>

                            {/*Input field for queueing codes*/}
                            <FormInput>

                            </FormInput>

                            {/*Enter button*/}
                            <button onClick={this.handleEnter}>Enter</button>
                        </div>
                    </div>
                    :
                    /*Logic for QR code scanning*/
                    <button onClick={this.handleToggle}>QR</button>
            }
            </div>
        )
    }
}
