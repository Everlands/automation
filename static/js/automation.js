function callService(service) 
{
   var data;
   $.get(service, function(response) {
        data = response;
   });

   return data;
}


