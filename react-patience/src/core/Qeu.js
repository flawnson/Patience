import React from "react"

import FormInput from "../components/inputs/FormInput.js"
import logo from "../Ouroboros.svg";


export default function Qeu () {
    return (
        <div>
            {/*Logo*/}
            <img src={logo} className="App-logo" alt="logo" />

            {/*Input field for queueing codes*/}
            <FormInput>

            </FormInput>

            {/*Enter button*/}
            <button>

            </button>

        </div>
    )
}
