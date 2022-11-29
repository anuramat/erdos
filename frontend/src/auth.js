import React from 'react';
import { Navigate } from 'react-router-dom';
import jwt_decode from "jwt-decode";

const key = "jwt";

export const setJWT = (token) => localStorage.setItem(key, token);

export const getJWT = () => localStorage.getItem(key);

export const getUserData = () => {
    const jwt = localStorage.getItem(key);
    let decoded = {};
    try {
        decoded = jwt_decode(jwt);
    } catch {
        logOut();
    }
    return decoded;
};

export const isAuthenticated = () => {
    return localStorage.getItem(key) !== null;
};

export const logOut = () => {
    localStorage.removeItem(key);
};

export const PrivateRoute = ({ children }) => {

    return isAuthenticated() ? children : <Navigate to="/" />;

};