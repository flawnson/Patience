import React from "react"

import styled from "styled-components"


export const FormGroup = styled.div`
	color: palevioletred;
    display: block;
	width: 300px;
	margin: 50px auto;
`;

export const Label = styled.label`
	margin-bottom: 0.5em;
	color: red;
    display: block;
`;


export const Input = styled.input`
	padding: 0.5em;
	color: blue;
	background: papayawhip;
	border: none;
	border-radius: 3px;
	width: 100%;
	margin-bottom: 0.5em;
`;

export const Message = styled.label`
	margin-bottom: 0.5em;
	color: green;
    display: block;
`;

export default function FormInput () {
    return (
        <div>
            <FormGroup>
                <Label>Label 2</Label>
                <Input />
                <Message>This is the validation message</Message>
            </FormGroup>
        </div>
    )
}
