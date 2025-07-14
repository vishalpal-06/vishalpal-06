/*
Update BlogState
class BlogState(TypedDict):
    title: str
    outline: str
    content: str
    evaluate: str


# Create evaluate_blog Function
def evaluate_blog(state: BlogState) -> BlogState:

    outline = state['outline']
    content = state['content']

    prompt = f'Based on the outline - {outline}, evaluate the blog content - {content} and provide feedback on how to improve it.'

    evaluation = llm.invoke(prompt).content
    state['evaluate'] = evaluation
    return state


# nodes
graph.add_node('create_outline', create_outline)
graph.add_node('create_blog', create_blog)
graph.add_node('evaluate_blog', evaluate_blog)

# edges
graph.add_edge(START, 'create_outline')
graph.add_edge('create_outline', 'create_blog')
graph.add_edge('create_blog', 'evaluate_blog')
graph.add_edge('evaluate_blog', END)
*/
