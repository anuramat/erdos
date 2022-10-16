import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { StartPage } from 'routes/startpage';
import { Registration } from 'routes/registration';
import { Login } from 'routes/login';

export const Router = () => {
    return (
        < Routes >
            <Route path='/registration' element={<Registration />} />
            <Route path="/login" element={<Login />} />
            <Route path="/" element={<StartPage />} />
        </Routes >
    )
}