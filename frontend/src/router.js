import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { Recent } from 'routes/recent';
import { Recommended } from 'routes/recommended';
import { Registration } from 'routes/registration';
import { Search } from 'routes/search';
import { PrivateRoute } from 'auth';

export const Router = () => {
    return (
        < Routes >
            <Route path="/" element={<Navigate replace to="/recent" />} />
            <Route path="/recommended" element={<PrivateRoute><Recommended /></PrivateRoute>} />
            <Route path="/recent" element={<Recent />} />
            <Route path="/registration" element={<Registration />} />
            <Route path="/search" element={<PrivateRoute><Search /></PrivateRoute>}> </Route>
        </Routes >
    )
}