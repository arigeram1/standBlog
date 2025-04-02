function like(slug){

    var likeElement = document.getElementById("like")
    var likeCounter = document.getElementById("like_counter")


   $.get(`/article/like/${slug}`).then(response => {

         if(response['response'] === "liked"){

             likeElement.className = 'fa fa-heart';

         }

         else{

             likeElement.className = 'fa fa-heart-o';

         }

         likeCounter.innerText = response['like_count'];

    })
}
