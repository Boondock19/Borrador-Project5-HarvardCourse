document.addEventListener("DOMContentLoaded",function(){
    get_comment=document.querySelector("#textarea_comment");
    get_comment_id=get_comment.getAttribute("data-article_id");
    comment_btn=document.querySelector("#comment-btn");
    article_content=document.querySelector("#content_article");
    comment_btn.addEventListener("click",function(){
        if (comment_btn.textContent=="Comment") {
            comment=get_comment.value;
            
        } 
        
        
    })
    
    function edit_Article(id,title,content){
        form= new FormData;
        form.append("title",title);
        form.append("content",content);
        fetch(`${id}`,{
            method:"POST",
            body:form,
        })
        .then((res) => res.json())
        .then((res) => {
            article_title.textContent=res.title2
            article_content.textContent=res.content2
        })  
    }
    

})