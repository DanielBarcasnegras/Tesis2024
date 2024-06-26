<?php

namespace App\Http\Controllers;

use App\Models\Image;

use Illuminate\Http\Request;

class StartController extends Controller
{

    public function index(){
        return view('Start',[
            'images' => Image::all()
        ]);
    }

}
