'use strict'

var fs = require('fs');
var path = require('path');
var args = require('yargs').argv;
var child_process = require('child_process');
var dotenv = require('dotenv').config();

var input_file = args.input || args.i || args._[0];
if(input_file === undefined)
{
	console.error('No input file supplied');
	process.exit(1);
}

var output_directory = args.output || args.o;
if(output_directory === undefined) output_directory = path.dirname(input_file);

var name = path.basename(input_file).split('.')[0];

var gltf_dir = output_directory + '/gltf';
if(!fs.existsSync(gltf_dir)) fs.mkdirSync(gltf_dir);

var usdz_dir = output_directory + '/usdz';
if(!fs.existsSync(usdz_dir)) fs.mkdirSync(usdz_dir);

var dae_dir = output_directory + '/dae';
if(!fs.existsSync(dae_dir)) fs.mkdirSync(dae_dir);

var gltf_path = gltf_dir + '/' + name + '.gltf';
var usdz_path = usdz_dir + '/' + name + '.usdz';
var dae_path = dae_dir + '/' + name + '.dae';

var task_finished = false;


function export_gltf()
{
	console.log('---- EXPORTING GLTF ------');

	var gltf_args = 
	[
		input_file,
		'--background',
		'--python',
		'blend_to_gltf.py',
		'--',
		gltf_path
	];

	run_blender(gltf_args);
}

function export_collada()
{
	console.log('---- EXPORTING DAE COLLADA ------');

	var collada_args = 
	[
		input_file,
		'--background',
		'--python',
		'blend_to_collada.py',
		'--',
		dae_path
	];

	run_blender(collada_args);
}

function export_usdz()
{
	console.log('---- EXPORTING USDZ ------');

    var usdz_args = 
	[
		'./libs/gltf2usd-master/Source/gltf2usd.py',
		'--arkit',
		'--optimize-textures',
		'-g',
		gltf_path,
		'-o',
		usdz_path
	];

    var usdz = child_process.spawn('python', usdz_args);
    /*
    usdz.stdout.on('data', function(data) 
	{
	    console.log(data.toString());
	});
	usdz.stderr.on('data', function(data) 
	{
	    console.error(data.toString());
	});
	*/
	usdz.on('close', function(data) 
	{
	    task_finished = true;
	});
}

function run_blender(args)
{
	task_finished = false;
	var blender_path = process.env.BLENDER;
	var blender = child_process.spawn(blender_path, args);

	/*
	blender.stdout.on('data', function(data) 
	{
	    console.log(data.toString());
	});
	blender.stderr.on('data', function(data) 
	{
	    console.error(data.toString());
	});
	*/

	blender.on('close', function(code) 
	{
		task_finished = true;
	});
}


var State = 
{
	INIT:0,
	GLTF:1,
	DAE:2,
	USDZ:3
};

var state = State.INIT;

function loop()
{
	switch(state)
	{
		case State.INIT:
		{
			export_gltf();
			state = State.GLTF;
			break;
		}
		case State.GLTF:
		{
			if(task_finished === true)
			{
				export_collada();
				state = State.DAE;
			}
			break;
		}
		case State.DAE:
		{
			if(task_finished === true)
			{
				export_usdz();
				state = State.USDZ;
			}
			break;
		}
		case State.USDZ:
		{
			if(task_finished === true)
			{
				process.exit(1);
				return;
			}
		}
	}
}
setInterval(loop, 0.1);
