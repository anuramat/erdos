import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Papers } from 'routes/papers';
import { Registration } from 'routes/registration';

export const Router = () => {
    return (
        < Routes >
            <Route path="/" element={<Papers />} />
            <Route path="/registration" element={<Registration />} />
        </Routes >
    )
}