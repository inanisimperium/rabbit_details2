var input = document.getElementById('input'),
			  button = document.getElementById('button'),
			  output = document.getElementById('output'),
			  data1 = 'Not ready to butcher';
			  data2 = 'Ready to butcher';

		      button.addEventListener("click", function() {
			  if(input.value <= '6') {
			      output.innerHTML = data1;
			  } else if (input.value >= '7') {
			      output.innerText = data2;
			  } else {
			      output.innerHTML = 'Nothing Found!';
			  }
		      });
