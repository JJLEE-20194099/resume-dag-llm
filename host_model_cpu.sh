# python -m vllm.entrypoints.openai.api_server --model TinyLlama/TinyLlama-1.1B-Chat-v1.0
# python -m vllm.entrypoints.openai.api_server --model HuggingFaceH4/zephyr-7b-beta --dtype bfloat16 --gpu-memory-utilization 0.5
python -m llama_cpp.server --model ./models/zephyr-7b-beta.Q5_K_M.gguf --chat_format chatml