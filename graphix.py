from graphviz import Digraph

# Create a visual mind map
dot = Digraph(comment='AI in Cloud Data Analytics', format='png')

# Main topic
dot.node('AI', 'Artificial Intelligence (AI)')

# Subfields
dot.node('ML', 'Machine Learning (ML)')
dot.node('DL', 'Deep Learning')
dot.node('LLM', 'Large Language Models (LLMs)')
dot.node('GenAI', 'Generative AI (GenAI)')

dot.edges([('AI', 'ML'), ('AI', 'DL'), ('DL', 'LLM'), ('DL', 'GenAI')])

# ML details
dot.node('Supervised', 'Supervised Learning\n(Labeled Data)')
dot.node('Unsupervised', 'Unsupervised Learning\n(Unlabeled Data)')
dot.edges([('ML', 'Supervised'), ('ML', 'Unsupervised')])

# Deep learning
dot.node('SemiSupervised', 'Semi-supervised Learning')
dot.edge('DL', 'SemiSupervised')

# LLM usage
dot.node('LLMTasks', 'Tasks:\n- Text generation\n- Summarization\n- Q&A')
dot.edge('LLM', 'LLMTasks')

# GenAI Applications
dot.node('GenAITypes', 'Types:\n- Text-to-Text\n- Text-to-Image\n- Text-to-Video\n- Text-to-Task\n- Multimodal')
dot.node('GenAIUses', 'Uses:\n- Chatbots\n- Predictive Modeling\n- Data Cleaning\n- Custom Analytics')
dot.edges([('GenAI', 'GenAITypes'), ('GenAI', 'GenAIUses')])

# Considerations
dot.node('Considerations', 'Considerations:\n- Data Quality\n- Ethics & Privacy\n- Human Oversight')
dot.edge('GenAI', 'Considerations')

# Cloud Data Analytics
dot.node('CloudUse', 'GenAI in Cloud Data Analytics')
dot.edge('GenAI', 'CloudUse')

# Render and display
dot.render('ai_cloud_data_analytics_mindmap', cleanup=True)
