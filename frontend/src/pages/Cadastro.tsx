import { useState } from "react";
import Header from "../components/Header";
import { toast } from "react-toastify";

type FormDataType = {
    name: string;
    email: string;
    password: string;
    role: string;
    profile_image: File | null;
};

export default function Cadastro() {
    const [formData, setFormData] = useState<FormDataType>({
        name: "",
        email: "",
        password: "",
        role: "",
        profile_image: null,
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value, type } = e.target;

        if (type === "file") {
            const file = (e.target as HTMLInputElement).files?.[0] || null;
            setFormData((prev) => ({ ...prev, profile_image: file }));
        } else {
            setFormData((prev) => ({ ...prev, [name]: value }));
        }
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        try {
            const data = new FormData();
            data.append("name", formData.name);
            data.append("email", formData.email);
            data.append("password", formData.password);
            data.append("role", formData.role);
            if (formData.profile_image) {
                data.append("profile_image", formData.profile_image);
            }

            const response = await fetch("http://localhost:5000/cadastro", {
                method: "POST",
                body: data,
            });

            const result = await response.json();
            if (response.ok) {
                toast.success("Cadastro realizado com sucesso!");
                console.log(result);
            } else {
                toast.error(`Erro: ${result.error}`);
            }
        } catch (error) {
            console.error("Erro ao cadastrar:", error);
            toast.error("Erro ao conectar com o servidor.");
        }
    };

    return (
        <div className="font-pressStart w-screen h-screen bg-charcoal flex flex-col items-center justify-center">
            <Header />
            <form
                onSubmit={handleSubmit}
                className="bg-darkSlate w-1/2 h-3/4 flex flex-col justify-center items-center rounded gap-4 p-6"
            >
                {/* Nome */}
                <input
                    name="name"
                    type="text"
                    placeholder="Nome"
                    value={formData.name}
                    onChange={handleChange}
                    className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                />

                {/* Email */}
                <input
                    name="email"
                    type="email"
                    placeholder="Email"
                    value={formData.email}
                    onChange={handleChange}
                    className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                />

                {/* Senha */}
                <input
                    name="password"
                    type="password"
                    placeholder="Senha"
                    value={formData.password}
                    onChange={handleChange}
                    className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                />

                {/* Função do usuário */}
                <select
                    name="role"
                    value={formData.role}
                    onChange={handleChange}
                    className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                >
                    <option value="">Selecione o papel</option>
                    <option value="0">Jogador</option>
                    <option value="1">Mestre</option>
                    <option value="2">Ambos</option>
                </select>

                {/* Imagem de perfil */}
                <input
                    name="profile_image"
                    type="file"
                    accept="image/*"
                    onChange={handleChange}
                    className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                />

                {/* Botão de cadastro */}
                <button
                    type="submit"
                    className="bg-deepRed hover:bg-forestGreen transition-colors text-offWhite rounded w-2/3 h-12 mt-4"
                >
                    Cadastrar
                </button>
            </form>
        </div>
    );
}
